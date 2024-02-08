1. Issue 1 - R tools installations 
- Installs Rtools
- Set Path 
Type in the R console 
- write('PATH="${RTOOLS40_HOME}\\usr\\bin;${PATH}"', file = "~/.Renviron", append = TRUE)
- Sys.which("make")
## "C:\\rtools40\\usr\\bin\\make.exe"
- install.packages("jsonlite", type = "source")

2. Issue 2 - There are binary versions available but the source versions are later: binary source needs_compilation
install.packages("packageName", type = "source") 