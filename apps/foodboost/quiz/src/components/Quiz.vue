<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>
    </p>
  </div>

  <div class="container">  
    <div class="row justify-content-center">
      <div class="col-md-4" align="center">
        <div class="card w-75 bg-image hover-overlay">

          <img src="https://static.ah.nl/static/recepten/img_RAM_PRD156799_1024x748_JPG.jpg" />
            <div class="card-img-top img-fluid rounded mask" style="background: linear-gradient( 45deg, rgba(29, 236, 197, 0.5), rgba(91, 14, 214, 0.5) 100% );" ></div>


          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">
              Some quick example text to build on the card title and make up the bulk
              of the card's content.
            </p>
          </div>
        </div> <!-- card end -->
      </div> <!-- col end -->

      <div class="col-md-4" align="center">
        <div class="card w-75">
          <img
            src="https://static.ah.nl/static/recepten/img_RAM_PRD156799_1024x748_JPG.jpg"
            class="card-img-top img-fluid rounded"
          />
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">
              Some quick example text to build on the card title and make up the bulk
              of the card's content.
            </p>
          </div>
        </div> <!-- card end -->
      </div> <!-- col end -->

  </div> <!-- row end -->


  <div class="row justify-content-center mt-4">
      <div class="col-md-4" align="center">
        <div class="card w-75">
          <img
            src="https://static.ah.nl/static/recepten/img_RAM_PRD156799_1024x748_JPG.jpg"
            class="card-img-top img-fluid rounded"
          />
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">
              Some quick example text to build on the card title and make up the bulk
              of the card's content.
            </p>
          </div>
        </div> <!-- card end -->
      </div> <!-- col end -->

      <div class="col-md-4" align="center">
        <div class="card w-75">
          <img
            src="https://static.ah.nl/static/recepten/img_RAM_PRD156799_1024x748_JPG.jpg"
            class="card-img-top img-fluid rounded"
          />
          <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="card-text">
              Some quick example text to build on the card title and make up the bulk
              of the card's content.
            </p>
          </div>
        </div> <!-- card end -->
      </div> <!-- col end -->

      

  </div> <!-- row end -->
</div>


</template>

<script>
export default {
  name: 'QuizComponent',
  props: {
    msg: String
  }
}
</script>

