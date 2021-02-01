# MPG - Master Plan Get
A simple tool to get data from Master Plan

## Notes:
### Requirements
- Uses request module to get data from the intranet.
- Requires to use browser cookie and session token.

## Usage:
- Set your cookie data on cookie.json file. (see cookie.json.sample)
```
usage: mpg.py [-h] -b BATCH [-d STARTDATE] [-o OUTFILE] -c COOKIEFILE

Holberton Intranet - Master Plan Get v.01.

optional arguments:
  -h, --help            show this help message and exit
  -b BATCH, --batch BATCH
                        Batch number. Required.
  -d STARTDATE, --date STARTDATE
                        Start date to fetch data (Format Y-m-d). Default: data_file.csv
  -o OUTFILE, --output OUTFILE
                        Output CSV file. Default: data_file.csv.
  -c COOKIEFILE, --cookiefile COOKIEFILE
                        Cookie File Name. Required.
```

### Return format from intranet
Array of data and links

```json
{
    "data": [
        {
            "id": "project-210",
            "_id": 210,
            "start_date": "25-01-2021 00:00",
            "end_date": "27-01-2021 00:00",
            "text": "0x00. Vagrant",
            "type": "project",
            "tags": ""
        },
        {
            "id": "project-210-sd",
            "_hide_tooltip": true,
            "start_date": "27-01-2021 00:00",
            "end_date": "30-01-2021 00:00",
            "text": "0x00. Vagrant",
            "color": "#93d1de",
            "type": "project-second-deadline",
            "tags": ""
        }
    ],
    "links": []
}
```

#### Types of data

```
"type": "day-off"
"type": "evaluation-quiz"
"type": "holiday"
"type": "nps-quiz"
"type": "peer_learning_day"
"type": "project"
"type": "project-second-deadline"
"type": "reefinery"
 ```

#### Projects

```json
{
    "id": "project-241",
    "_id": 241,
    "start_date": "04-05-2021 00:00",
    "end_date": "05-05-2021 00:00",
    "text": "0x03. Python - Data Structures: Lists, Tuples",
    "type": "project",
    "tags": ""
}
```

### Second Deadline

```json
{
    "id": "project-241-sd",
    "_hide_tooltip": true,
    "start_date": "05-05-2021 00:00",
    "end_date": "06-05-2021 00:00",
    "text": "0x03. Python - Data Structures: Lists, Tuples",
    "color": "#93d1de",
    "type": "project-second-deadline",
    "tags": ""
}
```

### PLD
```json
{
    "id": "peer_learning_day-42",
    "_id": 42,
    "start_date": "29-01-2021 00:00",
    "end_date": "30-01-2021 00:00",
    "text": "Shell - basics, permissions",
    "color": "purple",
    "type": "peer_learning_day"
}
```

### Evaluation / NPS Quiz
```json
{
    "id": "evaluation-quiz-1",
    "_id": 1,
    "start_date": "26-01-2021 00:00",
    "end_date": "27-01-2021 00:00",
    "text": "C quiz",
    "color": "#3ffabf",
    "type": "evaluation-quiz"
}
```
```json
{
    "id": "nps-quiz-1",
    "_id": 1,
    "start_date": "25-02-2021 00:00",
    "end_date": "26-02-2021 00:00",
    "text": "Student NPS after 1 month",
    "color": "#3ffabf",
    "type": "nps-quiz"
}
```

### Refinery (Mock)
```json
{
    "id": "reefinery-2",
    "_id": 2,
    "start_date": "02-02-2021 00:00",
    "end_date": "03-02-2021 00:00",
    "text": "0x00 - Shell",
    "color": "#FFB7C5",
    "type": "reefinery"
}
```

### Holiday / Day Off
```json
{
    "id": "holiday-2",
    "start_date": "24-07-2021 00:00",
    "end_date": "02-08-2021 00:00",
    "text": "Break #1",
    "color": "#f9c34e",
    "type": "holiday"
}
```
```json
{
    "id": "day-off-753",
    "start_date": "01-05-2021 00:00",
    "end_date": "02-05-2021 00:00",
    "text": "Labor Day",
    "color": "#f9c34e",
    "type": "day-off"
}
```

## TODO:
### DB Storage Structure
```sql
item
id varchar(50)
link_id int
start_date datetime
end_date datetime
text varchar(255)
color char(7)
type varchar(50)
tags varchar(100)
batch int

map_batch_cohort
batch
cohort
```

---
README.md - v.01