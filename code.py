class task:
  def search(cmd):
    tempcmd = cmd.split(";")
    sname = "null"
    spriority = "null"
    sproject ="null"
    leng = len(tempcmd)
    for i in range(leng):
      search = tempcmd[i].split("=")
      #print(search)
      if(search[0]=='name'):
        sname=search[1]
      if(search[0]=='p'):
        spriority=search[1]
      if(search[0]=='pn'):
        sproject=search[1]
    with open("test.txt",'r') as f:
      for line in f:
        temp = line.rstrip()
        temp = temp.split("/")
        if spriority != "null":
          if sproject != "null":
            if sname != "null":
              if spriority == temp[2] and sproject == temp[4] and sname==temp[0]:
                print(line)
            else:
              if spriority == temp[2] and sproject == temp[4]:
                print(line)
          else:
            if sname == "null":
              if spriority == temp[2]:
                print(line)
            else:
               if spriority == temp[2] and sname==temp[0]:
                print(line)
        else:
          if sproject != "null":
            if sname != "null":
              if sproject == temp[4] and sname==temp[0]:
                print(line)
            else:
              if sproject == temp[4]:
                print(line)
          else:
            if sname != "null":
              if sname==temp[0]:
                print(line)
  def FileInput(name,description,priority,date,project,status):
    with open("test.txt",'a')as f:
      f.write(name+"/"+description+"/"+priority+"/"+date+"/"+project+"/"+status+"\n")
