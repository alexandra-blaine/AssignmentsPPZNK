def setup():
    size(750,500)
    textSize(125)
    textAlign(CENTER)

        
def draw():
    
    if(((mouseX>=460 and mouseX<=540)and(mouseY>=25 and mouseY<=150))or keyPressed==True):
        fill(255,15,2)
        text("A",100,125)
    else:
        fill(127,7,196)
        text("A",100,125)
    
    text(" ",300,125)
    
    if(((mouseX>=60 and mouseX<=140)and(mouseY>=25 and mouseY<=150))or keyPressed==True):
        fill(255,175,2)
        text("B",500,125)
    else:
        fill(255,2,196)
        text("B",500,125)
        
    noFill()
    beginShape()
    curveVertex(45, 350)
    curveVertex(45, 350)
    curveVertex(100, 370)
    curveVertex(150, 380)
    curveVertex(200, 390)
    curveVertex(250, 400)
    curveVertex(300, 410)
    curveVertex(350, 420)
    curveVertex(400, 430)
    curveVertex(450, 440)
    curveVertex(500, 450)
    curveVertex(550, 460)
    curveVertex(600, 470)
    curveVertex(600, 470)
    endShape()
   
def keyPressed():
    if key==CODED:
        if keyCode==RIGHT: 
            fill(255,2,196)
            text("B",100,300)
            fill(127,7,196)
            text("A",500,300)
            


         
