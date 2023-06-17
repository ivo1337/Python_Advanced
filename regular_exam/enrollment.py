# def gather_credits(needed_credits, *courses):
#     enrolled_courses = []
#     gathered_credits = 0
#
#     for course in courses:
#         course_name, course_credits = course
#
#         if course_name in enrolled_courses:
#             continue
#
#         gathered_credits += course_credits
#         enrolled_courses.append(course_name)
#
#         if gathered_credits >= needed_credits:
#             break
#
#     if gathered_credits >= needed_credits:
#         enrolled_courses.sort()
#         return f"Enrollment finished! Maximum credits: {gathered_credits}.\nCourses: {', '.join(enrolled_courses)}"
#     else:
#         credits_shortage = needed_credits - gathered_credits
#         return f"You need to enroll in more courses! You have to gather {credits_shortage} credits more."



def gather_credits(needed_credits, *courses):
    enrolled_cours = []
    courses_credits = 0

    for course in courses:
        course_name, course_credits = course
        if courses_credits >= needed_credits:
            break

        if course_name not in enrolled_cours:
            enrolled_cours.append(course_name)
            courses_credits += course_credits

            if courses_credits >= needed_credits:
                break

    if courses_credits >= needed_credits:
        enrolled_cours.sort()
        return f"Enrollment finished! Maximum credits: {courses_credits}.\nCourses: {', '.join(enrolled_cours)}"
    else:
        credits_shortage = needed_credits - courses_credits
        return f"You need to enroll in more courses! You have to gather {credits_shortage} credits more."


