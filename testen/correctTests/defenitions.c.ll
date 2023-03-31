@a = dso_local global i32 10, allign 4
@b = dso_local global i32 a, allign 4
@c = dso_local global i8 97, allign 1
@temp = dso_local global float 20.5, allign 4
@ptr = dso_local global ptr @temp, allign 8 
