echo 'Step 1:'
grep -E '(.*[aeiou]){3}' input | grep -E '(\w)\1' | grep -vE '(ab|cd|pq|xy)' | wc -l
echo 'Step 2:'
cat input | grep -E '(..).*\1' | grep -E '(.).\1' | wc -l
