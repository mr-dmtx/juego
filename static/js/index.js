function Salvar(){
    let link = document.getElementById("txtLink").value;

    fetch("/", {
        method: "post",
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
      
        //make sure to serialize your JSON body
        body: JSON.stringify({
          link: link
        })
      })
      .then( () => { 
         window.location.reload();
      });

}