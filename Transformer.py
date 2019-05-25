import simplegui,random

x=0
v=0
a=0
b=0
t=0

#e:eyes
#h:head
#n:neck
#rh:right_hand
#lh:left_hand
#b:body
#l:leg
#rl:right_leg
#x:x co-ordinate
#y:y co-ordinate

rox,roy,rr=0,0,0
sx1,sy1,sx2,sy2=0,0,0,0
ex1,ex2,ey1,ey2,er=0,0,0,0,0
hx1,hx2,hx3,hx4=0,0,0,0
hy1,hy2,hy3,hy4=0,0,0,0
nx1,nx2,nx3,nx4=0,0,0,0
ny1,ny2,ny3,ny4=0,0,0,0
rhx,rhy1,rhy2,rhy3,rhy4=0,0,0,0,0
lhx,lhy1,lhy2,lhy3,lhy4=0,0,0,0,0
bx1,bx2,bx3,bx4,bx5,bx6,by1,by2,by3,by4,by5,by6=0,0,0,0,0,0,0,0,0,0,0,0
lx1,lx2,lx3,lx4,ly1,ly2,ly3,ly4=0,0,0,0,0,0,0,0
rlx1,rlx2,rlx3,rlx4,rly1,rly2,rly3,rly4=0,0,0,0,0,0,0,0
tx1,tx2,ty1,ty2=0,0,0,0,0,0,0,0

def draw(canvas):
    global t,rox,roy,rr,tx1,tx2,ty1,ty2,rlx1,rlx2,rlx3,rlx4,rly1,rly2,rly3,rly4,lx1,lx2,lx3,lx4,ly1,ly2,ly3,ly4,rhx,rhy1,rhy2,rhy3,rhy4,lhx,lhy1,lhy2,lhy3,lhy4,sx1,sy1,sx2,sy2,x,v,a,b,hx1,hy1,hx2,hy2,hx3,hx4,hy3,hy4,nx1,nx2,nx3,nx4,ny1,ny2,ny3,ny4,bx1,bx2,bx3,bx4,bx5,bx6,by1,by2,by3,by4,by5,by6,ex1,ex2,ey1,ey2,er
    for i in range(0,1):
        for j in range(0,1):
            a=random.randint(0,900)
            b=random.randint(0,400)
            canvas.draw_circle([a,b],2,1,"white","white")

    canvas.draw_circle([700,100],50,1,"yellow","white")
    canvas.draw_circle([730,80],50,1,"black","black")
    canvas.draw_polygon([[0,600],[0,510],[900,510],[900,600]],1,"#919191","#919191")
    canvas.draw_polygon([[850,510],[850,300],[870,300],[870,510]],3,"#919191","#ccc")
    canvas.draw_polygon([[850,300],[830,270],[850,240],[900,240],[930,270],[900,300]],3,"#919191","yellow")
   
    if v!=0 and x<200 and t!=1:
        canvas.draw_polygon([[447-x,462],[447-x,448],[0-x,360],[0-x,530]],1,"yellow","yellow")
   
    canvas.draw_circle([447-x+rox,455-roy],7-rr,1,"yellow","red")
    canvas.draw_polygon([[500-x+hx1,400-hy1],[550-x+hx2,350-hy2],[700-x-hx3,350-hy3],[750-x-hx4,400-hy4]],5,"gray","orange")
    canvas.draw_polygon([[450-x+bx1,480-by1],[450-x+bx2,430-by2],[500-x+bx3,400-by3],[750-x-bx4,400-by4],[800-x-bx5,430-by5],[800-x-bx6,480-by6]],5,"gray","orange")
    canvas.draw_circle([527.5-x+ex1,480-ey1],30-er,5,"gray","black")
    canvas.draw_circle([712.5-x-ex2,480-ey2],30-er,5,"gray","black")
    canvas.draw_polygon([[530-x+lx1,390+ly1],[560-x+lx2,360+ly2],[620-x-lx3,360+ly3],[620-x-lx4,390+ly4]],2,"gray","red")
    canvas.draw_polygon([[630-x+rlx1,390+rly1],[630-x+rlx2,360+rly2],[690-x-rlx3,360+rly3],[720-x-rlx4,390+rly4]],2,"gray","red")
    canvas.draw_polygon([[510-x-lhx,420-lhy1],[510-x-lhx,410-lhy2],[560-x-lhx,410-lhy3],[560-x-lhx,420-lhy4]],3,"gray","white")
    canvas.draw_polygon([[590-x+nx1,420-ny1],[590-x+nx2,410-ny2],[640-x-nx3,410-ny3],[640-x-nx4,420-ny4]],3,"gray","white")
    canvas.draw_polygon([[670-x+rhx,420-rhy1],[670-x+rhx,410-rhy2],[720-x+rhx,410-rhy3],[720-x+rhx,420-rhy4]],3,"gray","white")
    canvas.draw_line([550-x+sx1,390-sy1],[550-x+sx2,370-sy2],2,"white")
    canvas.draw_line([450-x+tx1,430-ty1],[800-x-tx2,430-ty2],5,"#ccc")
        
    x+=v

    if t==1:
        if hx1!=90:
            hx1+=1
        if hx2!=40:
            hx2+=1
        if hx3!=40:
            hx3+=1
        if hx4!=90:
            hx4+=1
        if hy1!=130:
            hy1+=1
        if hy2!=130:
            hy2+=1
        if hy3!=130:
            hy3+=1
        if hy4!=130:
            hy4+=1
            
        if nx1!=30:
            nx1+=1
        if nx2!=30:
            nx2+=1
        if nx3!=10:
            nx3+=1
        if nx4!=10:
            nx4+=1
        if ny1!=110:
            ny1+=1
        if ny2!=140:
            ny2+=1
        if ny3!=140:
            ny3+=1
        if ny4!=110:
            ny4+=1
        
        if ex1!=80:
            ex1+=1
        if ex2!=70:
            ex2+=1
        if ey1!=246:
            ey1+=2
        if ey2!=246:
            ey2+=2
        if er!=25:
            er+=1
            
        if sx1!=65:
            sx1+=1
        if sx2!=85:
            sx2+=1
        if sy1!=131:
            sy1+=1
        if sy2!=111:
            sy2+=1
            
        if bx1!=100:
            bx1+=1
        if bx2!=100:
            bx2+=1
        if bx3!=70:
            bx3+=1
        if bx4!=70:
            bx4+=1
        if bx5!=100:
            bx5+=1
        if bx6!=100:
            bx6+=1
        if by1!=80:
            by1+=1
        if by2!=100:
            by2+=1
        if by3!=90:
            by3+=1
        if by4!=90:
            by4+=1
        if by5!=100:
            by5+=1
        if by6!=80:
            by6+=1
            
        if lhx!=10:
            lhx+=1
        if lhy1!=30:
            lhy1+=1
        if lhy2!=40:
            lhy2+=1
        if lhy3!=80:
            lhy3+=1
        if lhy4!=70:
            lhy4+=1
            
        if rhx!=30:
            rhx+=1
        if rhy1!=70:
            rhy1+=1
        if rhy2!=80:
            rhy2+=1
        if rhy3!=40:
            rhy3+=1
        if rhy4!=30:
            rhy4+=1
        
        if lx1!=40:
            lx1+=1
        if lx2!=10:
            lx2+=1
        if lx3!=10:
            lx3+=1
        if lx4!=10:
            lx4+=1
        if ly1!=90:
            ly1+=1
        if ly2!=40:
            ly2+=1
        if ly3!=40:
            ly3+=1
        if ly4!=90:
            ly4+=1

        if rlx1!=10:
            rlx1+=1
        if rlx2!=10:
            rlx2+=1
        if rlx3!=10:
            rlx3+=1
        if rlx4!=40:
            rlx4+=1
        if rly1!=90:
            rly1+=1
        if rly2!=40:
            rly2+=1
        if rly3!=40:
            rly3+=1
        if rly4!=90:
            rly4+=1
            
        if tx1!=175:
            tx1+=1
        if tx2!=175:
            tx2+=1
        if ty1!=110:
            ty1+=1
        if ty2!=40:
            ty2+=1
           
        if rox!=183:
            rox+=1
        if roy!=135:
            roy+=1
        if rr!=2:
            rr+=1
def move():
    global v
    v=1
def stop():
    global v
    v=0
def trs():
    global t
    t=1
        
frame=simplegui.create_frame("Transformer",900,600)
frame.set_canvas_background("black")
frame.set_draw_handler(draw)
frame.add_button("move",move,100)
frame.add_button("stop",stop,100)
frame.add_button("Transform",trs,100)
frame.start()
