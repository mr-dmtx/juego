function assistir(){
    let section = document.getElementsByTagName("section");

    let iframe = document.createElement('iframe');
    iframe.src = document.getElementById("txtLink").value;
    iframe.width = "100%";
    iframe.height = "600"
    document.body.append(iframe);
    

}