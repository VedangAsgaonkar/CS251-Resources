import gdb

def printer(event):
    s = "+" + "-"*25 + "+";
    rsp = gdb.parse_and_eval("(uint8_t*)$rsp")
    rbp = gdb.parse_and_eval("(uint8_t*)$rbp")
    
    frame = gdb.selected_frame()
    while frame.older():
        frame = frame.older()
    
    old_rbp = frame.read_register('rbp')

    s +="\n|"
    for i in range(0,8*(int(old_rbp-rsp +7)//8)):
        if int((rsp+i).dereference())//16!=0:
            s+=" "+ hex(int((rsp+i).dereference())//16).lstrip("0x")
        else:
            s+=" 0"
        if int((rsp+i).dereference())%16!=0:
            s+=hex(int((rsp+i).dereference())%16).lstrip("0x")
        else:
            s+="0"
        if i%8==7 :
            if i==7:
                if (rbp-rsp)<8:
                    s+=" | <- rsp rbp"
                else:
                    s+=" | <- rsp"
            else:
                if i+rsp >= rbp and i+rsp-8< rbp:
                    s+=" | <- rbp"
                else:
                    s+=" |"
            s+="\n"
            s+="+" + "-"*25 + "+";
            s+="\n|"
    print(s[:-2])  
    return s
    

gdb.events.stop.connect(printer)
