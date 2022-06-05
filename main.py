import json
import csv

if __name__ == "__main__":

    outputfile = 'output.json'
    def get_file_contents_json(file):
        with open(file, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = {}  
            line = 0
            contents = []
            for row in csv_reader:
                key = str(line)
                data[key] = row
                line +=1
            contents = json.loads(json.dumps(data))

            return contents
    

    students = get_file_contents_json('students.csv')
    marks = get_file_contents_json('marks.csv')

    data = {}
    content = {}
    total_score = 0
    final_av = 0
    num_tests = 0
    key = "students"
    content["students"] = []
    for studs in students:
        
        for score in marks:
            
            if students[studs]['id'] == marks[score]['student_id']:
                total_score += int(marks[score]['mark'])
                num_tests += 1
            else:
                final_av = round(total_score/num_tests,2)
        data = {
            "ID": students[studs]['id'],
            "Name": students[studs]['name'],
            "Final Average": final_av
        }
        content[key].append(json.loads(json.dumps(data)))
    with open(outputfile, "w") as csv_file:
        json.dump(content,csv_file,indent=2)


    print('l')

    

    
    
    
    
    
    
    