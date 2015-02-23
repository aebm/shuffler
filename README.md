# shuffler
Python3 script to shuffle arguments or lines read.
Best used for doing fast contests or random picking.
Be advised that it does not remove duplicated input

## Examples

* Get a random order for a daily meeting

  ```bash
  ./shuffler.py Alice Bob Mallory Trent
  Alice
  Trent
  Mallory
  Bob
  ```

* Get the 5 cool persons

  ```bash
  ./shuffler.py < participants.txt | head -n 5
  Ada
  Barbara
  Alan
  Radia
  Edsger
  ```

* Run a contest

  ```bash
  ./shuffler < participants.txt > shuffled_participants.txt
  # Then read each line of shuffled participants until you get all your winners
  i=0
  while not finished; do
      head -n $i shuffled_participants.txt | tail -n 1
      i=$((i + 1))
  done
  ```
