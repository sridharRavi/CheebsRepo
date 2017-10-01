function doFirst()
{
	 barSize=600;
	 myMovie=document.getElementById('myMovie');
	 plButton=document.getElementById('play');
	 bar=document.getElementById('defaultbar');
	 progBar=document.getElementById('progBar');
	plButton.addEventListener('click',playOrPause,false);
	bar.addEventListener('click',clickedBar,false);
}
function playOrPause()
{
	if(!myMovie.paused && !myMovie.ended)
		{
			myMovie.pause();
			plButton.innerHTML='Play';
			window.clearInterval(updateBar)
		}
	else
	{
		myMovie.play();
		plButton.innerHTML='Pause';
		updateBar=setInterval(update,500);
	}
}
function update()
{
	if(!myMovie.ended)
	{
		var size=parseInt(myMovie.currentTime*barSize/myMovie.duration);
		progBar.style.width=size+'px';
	}
	else
		{
			progBar.style.width='0px';
			plButton.innerHTML='Play';
			window.clearInterval(updateBar);
		}
}
function clickedBar(e)
{
	if(!myMovie.paused && !myMovie.ended)
	{
		var mouseX=e.pageX-bar.offsetLeft;
		var newtime=mouseX*myMovie.duration/barSize;
		myMovie.currentTime=newtime;
		progBar.style.width=mouseX+'px';	

	}
}
window.addEventListener('load',doFirst,false);