# Example: ./start.sh 12

mkdir -p 2022/day-$1
cd 2022/day-$1
touch input.txt part1.py part2.py
git add .
git commit -m "Start 2022-day$1"