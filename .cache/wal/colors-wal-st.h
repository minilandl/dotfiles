const char *colorname[] = {

  /* 8 normal colors */
  [0] = "#3b1b22", /* black   */
  [1] = "#6C5DA4", /* red     */
  [2] = "#4E76C5", /* green   */
  [3] = "#9E6198", /* yellow  */
  [4] = "#C96F89", /* blue    */
  [5] = "#4B92C6", /* magenta */
  [6] = "#BC9FB7", /* cyan    */
  [7] = "#ddd2de", /* white   */

  /* 8 bright colors */
  [8]  = "#9a939b",  /* black   */
  [9]  = "#6C5DA4",  /* red     */
  [10] = "#4E76C5", /* green   */
  [11] = "#9E6198", /* yellow  */
  [12] = "#C96F89", /* blue    */
  [13] = "#4B92C6", /* magenta */
  [14] = "#BC9FB7", /* cyan    */
  [15] = "#ddd2de", /* white   */

  /* special colors */
  [256] = "#3b1b22", /* background */
  [257] = "#ddd2de", /* foreground */
  [258] = "#ddd2de",     /* cursor */
};

/* Default colors (colorname index)
 * foreground, background, cursor */
 unsigned int defaultbg = 0;
 unsigned int defaultfg = 257;
 unsigned int defaultcs = 258;
 unsigned int defaultrcs= 258;
