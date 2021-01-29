#!/bin/bash

#repetir até obter arquivo executável
#repeat until get .exe file
while true;
do
    directory=$(zenity --file-selection --file-filter="Arquivo executável (exe) | *.exe" --title="Selecione o executável:" --filename="/home/$USERNAME/.wine/drive_c/")
    if [ $? -eq 0 ]
    then
        break;
    else
        $(zenity --question --text="Você tem que selecionar um arquivo executável para continuar. Deseja tentar novamente?")
        if [ $? -ne 0 ]
        then
            exit
        fi 
    fi
done

devpath=$(find /sys/class/hidraw ! -path /sys/class/hidraw -name 'hidraw'*)

#http://www.linuxquestions.org/questions/programming-9/reading-lines-to-an-array-and-generate-dynamic-zenity-list-881421/
   
mode="true"
choices=()

#Ler cada arquivo de texto em dp/device/uevent para descobrir o nome do dispositivo
#Read each text file in dp/device/uevent to discover device name
#OBS: Tanto dp como devpath armazenam o caminho da pasta, não só o nome
#OBS: the variables called "dp" and "devpath" in this foreach store the complete path of the folders, not only theirs name

for dp in ${devpath}
do   
    #Obtem o nome da pasta a partir do caminho armazenado em "dp"
    #Get the folder name through the path stored in "dp"
    foldername=$(basename "$dp")
    #Lê /sys/class/hidraw/hidraw[#]/device/uevent a procura de seu Hid_name  
    #Read /sys/class/hidraw/hidraw[#]/device/uevent serching for HID_NAME
    devname=$(grep -oP 'HID_NAME=\K.*' $dp/device/uevent)
    #Vetor que atualiza a cada iteração para preencher a lista dispositivos no zenity --radiolist
    #Array that updates each iteration to fill the device list in zenity --radiobox
    choices=("${choices[@]}" "$mode" "$devname")
	mode="false"    
done

#repetir até obter nome do dispositivo
#repeat until get device name
while true;
do
    choice=$(zenity \
	    --list \
	    --radiolist \
	    --text="Dispositivos conectados:" \
	    --column "" \
	    --column "Dispositivos: " \
	    "${choices[@]}")

    if [ $? -eq 0 ]
    then
        break;
    else
        $(zenity --question --text="Você tem que selecionar um dispositivo para continuar. Deseja tentar novamente?")
        if [ $? -ne 0 ]
        then
            exit
        fi 
    fi
done

filename=$(basename "$directory")
filename="${filename%%.*} script"

#cria um script para aquele programa/dispositivo
#creates a script to that program/device

cat > "$filename.sh" << End_Script
#!/bin/bash

#https://wiki.winehq.org/Hid

function startApp 
{
    su \$USERNAME
    wine cmd
    wine net start winebus
    #transforma o caminho em linux para wine (como se fosse no windows)
    #Transform the path from linux to wine
    wine start "c:${directory#*drive_c}"
    exit
}

function devNotFound
{
    \$(zenity --question --text="Dispositivo não foi achado, Deseja repetir procedimento?")
    if [ \$? -eq 0 ]
    then
        searchDevice
    else 
        exit
    fi         
    
}

function searchDevice 
{
    #Obtem lista de pastas dentro de /sys/class/hidraw excluindo ela mesma
    #Get the folder list inside /sys/class/hidraw excluding itself
    #A lista de dispositivos HID é variavel,por isso refaz os passos toda vez ao executar o script
    #The HID list is changeable, therefore it has to repeat these steps each execution
    devpath=\$(find /sys/class/hidraw ! -path /sys/class/hidraw -name 'hidraw'*)

    #Ler cada arquivo de texto em dp/device/uevent para descobrir o nome do dispositivo
    #Read each text file in dp/device/uevent to discover device name
    #OBS: Tanto dp como devpath armazenam o caminho da pasta não só o nome
    #OBS: the variables called "dp" and "devpath" in this foreach store the complete path of the folders, not only theirs name
    for dp in \${devpath}
    do   
        #Obtem o nome da pasta a partir do caminho armazenado em "dp"
	#Get the folder name through the path stored in "dp"
        foldername=\$(basename "$dp")
        #Lê a terceira linha de /sys/class/hidraw/hidraw[#]/device/uevent 
	#Read /sys/class/hidraw/hidraw[#]/device/uevent serching for HID_NAME
        #http://stackoverflow.com/questions/7996629/how-do-i-read-the-nth-line-of-a-file-and-print-it-to-a-new-file          
        devicename=\$(sed -n '3{p;q;}' \$dp/device/uevent)
        if [[ "\$devicename" == *"$devname" ]]
        then
            #Dá permissão ao dispositivo hid
	    #Give permission to HID
            #Só funciona com 777, go+rw fica carregando, mas não funciona (averiguado apenas no dispositivo testado)
	    #Only works with 777. go+rw keep loading, but does not work (with the tested device)
            pkexec chmod 777 /dev/\$foldername            
            startApp
            break
        fi
    done
    
    devNotFound
}

searchDevice

exit

End_Script

$(zenity --info --text="Script gerado com sucesso! Execute-o para executar a aplicação como dispositivo")

exit


