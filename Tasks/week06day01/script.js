function Teacher(_ad,_soyad,_yas){
    this.ad=_ad
    this.soyad=_soyad
    this.yas=_yas
    this.melumatGoster=function(){
      console.log(this.ad,this.soyad,this.yas)
    }
  }

  muellim=Teacher("Murad","Mustafayev","34");

  console.log(muellim)