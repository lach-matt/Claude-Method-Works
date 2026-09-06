P='3d6 ?4s2|3d7 ?4s2|4f7 ?6s2|4f13 ?6s2|4f6 ?6s2|4f8 ?6s2|4f12 ?6s2|5d ?6s2|8S7/2|La II|Ce II|Pr II|Nd II|Sm II|Eu II|Gd II|Tb II|Dy II|Ho II|Er II|Tm II|Lu II|Co II|Ni II|Yb II|MZH78|Martin.{0,20}Zalubas|SC85|hole.state|hole state'
for f in /mnt/project/*; do n=$(grep -c -i -E "$P" "$f" 2>/dev/null); echo "$n  $(basename "$f")"; done
echo --- archives
grep -r -l -i -E "$P" /home/claude/arch --include='*' 2>/dev/null | grep -v pycache | sed 's#/home/claude/arch/##'