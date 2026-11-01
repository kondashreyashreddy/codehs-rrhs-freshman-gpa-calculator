from cn import english, lote, science, social_studies, cte, math
from var import cc, per, cn_list, cnt, cn_list, gpa_list, chlorine, clorox, cwn, ug, gpa, per1, per2, per3, per4, per5, per6, per7, per8, per1_grade, per2_grade, per3_grade, per4_grade, per5_grade, per6_grade, per7_grade, per8_grade, tstore

def reset():
    global ug, cc, cnt, tstore
    ug = 0
    cc = 0
    cnt = "None"
    tstore = 0
    
def saving():
    global ug, cnt, per1, per2, per3, per4, per5, per6, per7, per8, per1_grade, per2_grade, per3_grade, per4_grade, per5_grade, per6_grade, per7_grade, per8_grade
    if per == 1:
        per1_grade = ug
        per1 = cnt
    elif per == 2:
        per2_grade = ug
        per2 = cnt
    elif per == 3:
        per3_grade = ug
        per3 = cnt
    elif per == 4:
        per4_grade = ug
        per4 = cnt
    elif per == 5:
        per5_grade = ug
        per5 = cnt
    elif per == 6:
        per6_grade = ug
        per6 = cnt
    elif per == 7:
        per7_grade = ug
        per7 = cnt
    elif per == 8:
        per8_grade = ug
        per8 = cnt
    
def gpa_calc():
    global cwn, gpa, ug, clorox
    if clorox != 0:
        cwn = cwn + 1
        saving()
        tstore = ug * (0.01 * clorox)
        gpa = gpa + tstore
    else:
        saving()
    
def program_end():
    print("----------------------------------------------------------")
    print("                      PROGRAM END")
    print("----------------------------------------------------------")

def course():
    global cc, per
    print("----------------------------------------------------------")   
    cc = int(input(f"Which Course Category Would You Like To Chose For Class Period {per}?\n1. English\n2. Languages Other Than English\n3. Science\n4. Social Studies\n5. Career & Technical Education\n6. Mathematics\nType A Number: "))
    if cc == 1:
        english()
    elif cc == 2:
        lote()
    elif cc == 3:
        science()
    elif cc == 4:
        social_studies()
    elif cc == 5:
        cte()
    elif cc == 6:
        math()
    else:
        course()

def course_grade():
    global cnt, clorox, ug, chlorine
    cnt = input("Copy + Paste Course Name Here: ")
    if cnt in cn_list:
        for chlorine in cn_list:
            if chlorine == cnt:
                sc = cn_list.index(chlorine)
                clorox = gpa_list[sc]
                ug = int(input(f"\nEnter Class Grade For {cnt}: "))
                gpa_calc()
                reset()
    else:
        course_grade()
    
def per_one():
    global per
    per = 1
    course()
    course_grade()
    
def per_two():
    global per
    per = 2
    course()
    course_grade()
    
def per_three():
    global per
    per = 3
    course()
    course_grade()
    
def per_four():
    global per
    per = 4
    course()
    course_grade()
    
def per_five():
    global per
    per = 5
    course()
    course_grade()
    
def per_six():
    global per
    per = 6
    course()
    course_grade()
    
def per_seven():
    global per
    per = 7
    course()
    course_grade()
    
def per_eight():
    global per
    per = 8
    course()
    course_grade()
    
def fin_print():
    global gpa
    gpa = gpa/cwn
    print("----------------------------------------------------------")
    print(f"Period 1: {per1} ---- Grade: {per1_grade}")
    print(f"Period 2: {per2} ---- Grade: {per2_grade}")
    print(f"Period 3: {per3} ---- Grade: {per3_grade}")
    print(f"Period 4: {per4} ---- Grade: {per4_grade}")
    print(f"Period 5: {per5} ---- Grade: {per5_grade}")
    print(f"Period 6: {per6} ---- Grade: {per6_grade}")
    print(f"Period 7: {per7} ---- Grade: {per7_grade}")
    print(f"Period 8: {per8} ---- Grade: {per8_grade}")
    print(f"\nGPA: {gpa}/6.0")
    print(f"you have {cwn} weighted classes")
    program_end()
    
