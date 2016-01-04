var x=150;
var y=70;
var dx=1;
var dy=0.5;
var flag=0;
var flag1=0;
var currentT = new Date()
var previousTime=currentT.getTime();
var f= function()
{
var canvas=document.getElementsByTagName('canvas')[0];
var c=canvas.getContext('2d');
c.font="10px Calibri";


setTimeout(draw,10);	
//displaytime();
};	

function draw()
{  
 
var canvas=document.getElementsByTagName('canvas')[0];
var c=canvas.getContext('2d');

c.clearRect(0,0, 1000,600);
   n();
  
   //displaytime();  

  c.beginPath();
  // Draws a circle of radius 20 at the coordinates 100,100 on the canvas
  c.arc(x,y,5,0,Math.PI*2,true);
  c.stroke();
  c.closePath();
  //c.fill();
  //x+=dx;
  
    var currentTime = new Date()
	var hours = currentTime.getHours()
	var minutes = currentTime.getMinutes()
    var seconds = currentTime.getSeconds()
	var exitTime=currentTime.getTime();
	
var tim="Time: "+ hours+":"+ minutes+":"+seconds;
c.strokeText(tim, 90,155);
 
  var pause=50;
  var message=tim;
  if(y>=69 && y<=95 && flag==0 && x<=155)
  {
	  if(y==70)
	  {
		  
		  pause=500;//stadium
		  var u=new Date()
		  var sec=u.getTime()-previousTime;
		  //previousTime=u.getTime();
		  message=(sec/100)+ "Seconds";
	  }
	  	  y=y+1;
  }
	
  
  else if(y>=95 && flag==0 && x<=420 && flag1==0)
  {
	
if(x==352)
{	
	pause=5000;//alumni center
	var nu=new Date()
		  var sec=nu.getTime()-previousTime;
		  //previousTime=u.getTime();
		  message=(sec/100)+ "Seconds";
}	
x=x+1;

	
  }
  
  else if(x>=420 && flag==0 && y<=295)
  { 
	  if(y==116 || y==186 || y==277)
	  {		
		  pause=5000;//briscoe , Mcnutt, kelly
		  var u=new Date()
			var sec=u.getTime()-previousTime;
		  message=sec/100;
		  
	  }	 
	  y=y+1;
  }
  
  else if(y>=295 && flag==0 && x<=495)
  {
	  if(x==490)
	{ 
	pause=5000;
	var u=new Date()
	var sec=u.getTime()-previousTime;
	sec= sec/100;
	sec=" Seconds: "+sec;
	message=sec;

	}
	  x=x+1;
	  //flag=1;
  }
  
  else if(x>=495 && y<=495)
{
	if(y==410 || y==490)
	{ 
	pause=5000;
	var u=new Date()
	var sec=u.getTime()-previousTime;
	sec= sec/100;
	sec=sec+" Seconds"
	message=sec;
	}
	  y=y+1;
	  flag=1;
}

else if(y>=495 && flag==1 && x>=205 && flag1==0)
{
	if(x==345)
	{
	pause=5000;
	var u=new Date()
	var sec=u.getTime()-previousTime;
	message=sec/100+" Seconds";
	}
	x=x-1;	
}

else if(y>=405 && flag==1 && x<=205 && flag1==0)
{
	if(y==485 || y==465)
	{
	pause=5000;
	var u=new Date()
	var sec=u.getTime()-previousTime;
	message=sec;
	}
	y=y-1;	
}
  
  else if(y<=405 && flag==1 && x<=295 && flag1==0)
  {
	  if(x==290)
	{
	pause=5000;
	var u=new Date()
	var sec=u.getTime()-previousTime;
	message=sec;
	}
	  x=x+1;
  }
  
  else if(y>=305 && flag==1 && x>=295 && flag1==0)
{
	y=y-dy;	
}
 else if(y<=305 && flag==1 && x<=420 && flag1==0)
  {
	   if(x==400)
	{
	pause=5000;
	var u=new Date()
	var sec=u.getTime()-previousTime;
	message=sec;
	}
	  x=x+1;
  }
  
else if(x>=420 && flag==1 && y>=105)
{
	if(y==280 || y==190 || y==115)
	{
	pause=5000;
	var u=new Date()
	var sec=u.getTime()-previousTime;
	message=sec;
	}
y=y-1;
flag1=1;	
}

else if(x>=155 && y<=105 && flag1==1)
{
	if(x==375)
	{
	pause=5000;
	var u=new Date()
	var sec=u.getTime()-previousTime;
	message=sec;																																			
	}
	x=x-1;
}

else if(x<=155 && y>=70 && flag1==1)
{
	y=y-1;
	if(y<=70)
	{
		flag=0;
		flag1=0;
	}
}
  setTimeout(draw,pause);
  document.getElementById('message').innerHTML=message;
};


function pause(numberMillis) { 
var canvas=document.getElementsByTagName('canvas')[0];
var c=canvas.getContext('2d');

	
    var now = new Date(); 
	var nowT=now.getTime();


    var exitTime = now.getTime() + numberMillis; 
	setTimeout(function(){
		c.fillText("Hi");
	},numberMillis)	
	

};

var displaytime= function()
{
	var canvas=document.getElementsByTagName('canvas')[0];
	var c=canvas.getContext('2d');
	var currentTime = new Date()
	var hours = currentTime.getHours()
	var minutes = currentTime.getMinutes()
    var seconds = currentTime.getSeconds()
	
	if (minutes < 10)
	minutes = "0" + minutes
c.strokeText(("Time: "+ hours+":"+ minutes+":"+seconds), 75, 80);
	
};

var n= function()
{
	var canvas=document.getElementsByTagName('canvas')[0];
	var c=canvas.getContext('2d');
	c.strokeText("Memorial Stadium",165,70);

	
	c.beginPath();
	c.arc(160,70,3,0,2*Math.PI);
	c.stroke();
	
	c.strokeText("Assembly Hall",380,90);
	
	c.beginPath();
	c.arc(375,90,3,0,2*Math.PI);
	c.stroke();
	
	c.strokeText("Alumni Center",285,110);
	
	c.beginPath();
	c.arc(350,110,3,0,2*Math.PI);
	c.stroke();
	
	c.strokeText("Briscoe",440,120);
	
	c.beginPath();
	c.arc(435,120,3,0,2*Math.PI);
	c.stroke();
	
	c.strokeText("Briscoe",380,115);
	
	c.beginPath();
	c.arc(415,115,3,0,2*Math.PI);
	c.stroke();
	
	c.strokeText("Foster",440,190);
	
	c.beginPath();
	c.arc(435,190,3,0,2*Math.PI);
	c.stroke();
	
	c.strokeText("McNutt",375,190);
	
	c.beginPath();
	c.arc(415,185,3,0,2*Math.PI);
	c.stroke();
	
	c.strokeText("Kelley School of Business",440,280);
	
	c.beginPath();
	c.arc(435,280,3,0,2*Math.PI);
	c.stroke();
	
	c.strokeText("Kelley School of Business",305,275);
	
	c.beginPath();
	c.arc(415,275,3,0,2*Math.PI);
	c.stroke();
	
	c.strokeText("Wells",460,315);
	c.strokeText("Library",460,325);
	
	c.beginPath();
	c.arc(490,310,3,0,2*Math.PI);
	c.stroke();
	
	c.strokeText("Neal-",445,410);
	c.strokeText("Marshall",445,420);
	
	c.beginPath();
	c.arc(490,410,3,0,2*Math.PI);
	c.stroke();
	
	c.strokeText("3rd &",460,480);
	c.strokeText("Jordan",455,490);
	
	c.beginPath();
	c.arc(490,490,3,0,2*Math.PI);
	c.stroke();
	
	c.strokeText("Jordan Hall",330,480);
	
	c.beginPath();
	c.arc(350,490,3,0,2*Math.PI);
	c.stroke();
	
	c.strokeText("Maurer School",220,485);
	c.strokeText("Of law",220,495);
	
	c.beginPath();
	c.arc(210,490,3,0,2*Math.PI);
	c.stroke();
	
	c.strokeText("Sample Gates",220,465);
	
	c.beginPath();
	c.arc(210,465,3,0,2*Math.PI);
	c.stroke();
	
	c.strokeText("IMU",282,425);
	
	c.beginPath();
	c.arc(290,410,3,0,2*Math.PI);
	c.stroke();
	
	c.strokeText("Psychology",375,325);
	
	c.beginPath();
	c.arc(400,310,3,0,2*Math.PI);
	c.stroke();
	
	c.beginPath();	
	c.moveTo(300,300);
	c.lineTo(500,300);
	c.stroke();
	
	c.beginPath();	
	c.moveTo(500,300);
	c.lineTo(500,500);
	c.stroke();
	
	c.beginPath();	
	c.moveTo(500,500);
	c.lineTo(200,500);
	c.stroke();
	
	c.beginPath();	
	c.moveTo(200,500);
	c.lineTo(200,400);
	c.stroke();
	
	c.beginPath();	
	c.moveTo(200,400);
	c.lineTo(300,400);
	c.stroke();
	
	c.beginPath();	
	c.moveTo(300,400);
	c.lineTo(300,300);
	c.stroke();

	c.beginPath();	
	c.moveTo(425,300);
	c.lineTo(425,100);
	c.stroke();
	
	c.beginPath();	
	c.moveTo(425,100);
	c.lineTo(150,100);
	c.stroke();
	
	c.beginPath();	
	c.moveTo(150,100);
	c.lineTo(150,70);
	c.stroke();
	
	
	c.beginPath();
	var neel=c.arc(150,70,3,0,2*Math.PI);
	c.stroke(); 	
	
};


window.addEventListener('load',f,false);