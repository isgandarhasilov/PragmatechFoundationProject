// console.log("Hello World!")


let button = document.getElementById("button");
button.addEventListener("click", yaziYazdir);

  function yaziYazdir() {
    document.getElementById("text").innerHTML += "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Neque dolorem, molestias deleniti aperiam similique dolorum nihil et veritatis quae, nobis sint reprehenderit numquam voluptatem enim perspiciatis dicta aut quam tenetur?";
  }