var video, canvas, context, imageData;
  
    function onLoad(){
      video = document.getElementById("video");
      canvas = document.getElementById("canvas");
      context = canvas.getContext("2d");
    
      canvas.width = parseInt(canvas.style.width);
      canvas.height = parseInt(canvas.style.height);
      
      navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia;
      if (navigator.getUserMedia){
        
        function successCallback(stream){
          if (window.webkitURL) {
            video.src = window.webkitURL.createObjectURL(stream);
          } else if (video.mozSrcObject !== undefined) {
            video.mozSrcObject = stream;
          } else {
            video.src = stream;
          }
        }
        
        function errorCallback(error){
        }
        
        navigator.getUserMedia({video: true}, successCallback, errorCallback);

        requestAnimationFrame(tick);
      }
    }
    
    function tick(){
      requestAnimationFrame(tick);
           if (video.readyState === video.HAVE_ENOUGH_DATA){
        snapshot();
      }
    }

    function snapshot(){
      context.drawImage(video, 0, 0, canvas.width, canvas.height);
      imageData = context.getImageData(0, 0, canvas.width, canvas.height);
    }
          
    window.onload = onLoad;