
*bspwm* is a tiling window manager that represents windows as the leaves of a full binary tree.

It only responds to X events, and the messages it receives on a dedicated socket.

*bspc* is a program that writes messages on *bspwm*'s socket.

*bspwm* doesn't handle any keyboard or pointer inputs: a third party program (e.g. *sxhkd*) is needed in order to translate keyboard and pointer events to *bspc* invocations.

The outlined architecture is the following:

```
        PROCESS          SOCKET
sxhkd  -------->  bspc  <------>  bspwm
```

## Configuration

The default configuration file is `$XDG_CONFIG_HOME/bspwm/bspwmrc`: this is simply a shell script that calls *bspc*.

What this config looks like.

![image](https://user-images.githubusercontent.com/47686364/111281218-aa38a000-8677-11eb-85da-d94431521fb2.png)


![image](https://user-images.githubusercontent.com/47686364/111281445-e79d2d80-8677-11eb-81ef-271486b53432.png)



![image](https://user-images.githubusercontent.com/47686364/111281492-f1bf2c00-8677-11eb-9914-4f4ad169db4b.png)

