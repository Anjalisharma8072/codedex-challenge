def dompier_music(switches):
    
    fq = {
        261: "C4",
        294: "D4",
        329: "E4",
        349: "F4",
        392: "G4",
        440: "A4",
        494: "B4",
        523: "C5",
        0: "REST"
    }
  
    notes = []
    
    for i in range(len(switches)):
        decimal = 0
        j = 0
        binary = switches[i]
        
        for k in range(len(binary)-1, -1, -1):
            num = int(binary[k])
            decimal += num * (2 ** j)
            j += 1
        
        notes.append(fq[decimal])
    
    return notes