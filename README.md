# ZoomClassPicker

Quick python program that will pick the next zoom link based on time and day of the week

## Installation

git clone the repository, edit the link_aulas.txt file with the proper format and run the main.py

make sure you are using python3

has not been tested in linux yet

## Format for link_aulas.txt
order of paramenters (are the values are seperated by c','):
1. Link for video class
2. Name of the class
3. Day of the week (1 - Monday; 2 - Tuesday....)
4. Time (11h00; 15h00; 17h00...)
5. ';'

exemple of a line:
```bash
https://zoom.com,MO-T,2,15h00;'\n'
```



## License
[MIT](https://choosealicense.com/licenses/mit/)
