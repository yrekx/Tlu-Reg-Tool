import Variable_stored
import json


def Show_All_Subjects(semester_register_periods):
    i = 0
    for period in semester_register_periods:
    
        if isinstance(period, dict):
            
            print(f"sub[{i}]: {period.get('subjectName')}")
            i+=1
            Variable_stored.subject_name.append(period.get('subjectName'))




def show(subject,indexSelected):            
    global S_DICT
    global simplified_data
    count = 0
    
    content = subject.get('courseRegisterViewObject', {})
    

    if isinstance(content, dict):
        semester_register_periods = content.get('listSubjectRegistrationDtos', [])        
        if isinstance(semester_register_periods, list):
            print('still good')
            print(f'Press F{Variable_stored.subject_name[indexSelected]}')
            print(semester_register_periods)
            for period in semester_register_periods:
                if isinstance(period, dict):  
                    if period.get('subjectName') == Variable_stored.subject_name[indexSelected]:
                        course_subjects = period.get('courseSubjectDtos', [])
                        
                        if isinstance(course_subjects, list):
                            for course_subject in course_subjects:
                                if isinstance(course_subject, dict):
                                    timetables = course_subject.get('timetables', [])                                
                                    if isinstance(timetables, list):
                                        print(f"------------------------[{course_subject.get('displayName')} ({course_subject.get('numberStudent')}/{course_subject.get('maxStudent')})]----------------------------")
                                        print(f"SUB[{count}]")
                                        count+=1
                                        for timetable in timetables:
                                            
                                            if isinstance(timetable, dict):
                                                start_time = Variable_stored.convert_timestamp(timetable.get('startHour', {}).get('start', 0))
                                                end_time = Variable_stored.convert_timestamp(timetable.get('endHour', {}).get('end', 0))
                                                print(f"From week {timetable.get('fromWeek')} to {timetable.get('toWeek')} \t\t\tWeek index: {timetable.get('weekIndex')} \t Start: {start_time} End: {end_time}\tRoom: {timetable.get('roomName')}")                                               
                                    
                                    print(f"Teacher: {timetable.get('teacherName')}")                  
                                    print(f"Course Subject ID: {course_subject.get('id')}")                            
                                    
                                try:
                                    i = 0
                                    subCourseSub = course_subject.get('subCourseSubjects',[])
                                    for subcourse in subCourseSub:
                                        timetables = subcourse.get('timetables',[])
                                        print(f"subCourse[{i}]\t\t{subcourse.get('displayName')}")
                                        i+=1
                                        
                                        for timetable in timetables:
                                            start_time = Variable_stored.convert_timestamp(timetable.get('startHour', {}).get('start', 0))
                                            end_time = Variable_stored.convert_timestamp(timetable.get('endHour', {}).get('end', 0))
                                            print(f"From week {timetable.get('fromWeek')} to {timetable.get('toWeek')} \t\t\tWeek index: {timetable.get('weekIndex')} \t Start: {start_time} End: {end_time}\tRoom: {timetable.get('roomName')}")
                                except:
                                    pass
                        try:           
                            if i==0:
                                index = int(input("Enter Subject_Course: "))
                                Variable_stored.simplified_data = course_subjects[index]
                            else:
                                
                                index = int(input("Enter Sub: "))
                                subIndex = int(input("Enter SubCourse: "))
                                for subCourse in course_subjects:
                                    simplified_data = subCourse.get('subCourseSubjects',[])
                                    if index == 0:
                                        break
                                    index -=1
                                Variable_stored.simplified_data = simplified_data[subIndex]
                                
                        except:
                            pass


