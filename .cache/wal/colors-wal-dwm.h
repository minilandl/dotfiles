static const char norm_fg[] = "#ddd2de";
static const char norm_bg[] = "#3b1b22";
static const char norm_border[] = "#9a939b";

static const char sel_fg[] = "#ddd2de";
static const char sel_bg[] = "#4E76C5";
static const char sel_border[] = "#ddd2de";

static const char urg_fg[] = "#ddd2de";
static const char urg_bg[] = "#6C5DA4";
static const char urg_border[] = "#6C5DA4";

static const char *colors[][3]      = {
    /*               fg           bg         border                         */
    [SchemeNorm] = { norm_fg,     norm_bg,   norm_border }, // unfocused wins
    [SchemeSel]  = { sel_fg,      sel_bg,    sel_border },  // the focused win
    [SchemeUrg] =  { urg_fg,      urg_bg,    urg_border },
};
