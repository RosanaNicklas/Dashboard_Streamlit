
import os

# No subir los datos al github


ENTORNO=os.environ["USERNAME"]
ENTORNOJAVI="Matolo"
ENTORNOROSANA="Rosana"
ENTORNOLOCAL=os.environ["USERNAME"]==ENTORNOJAVI or ENTORNOROSANA
INIDATABASE="postgres"
DATABASE="dashboard"
IRISTABLE="iris"
IRISCOLLIST=['Id', 'PetalLengthCm', 'PetalWidthCm', 'SepalLengthCm', 'SepalWidthCm','Species']
IRISCOL1="Id"
IRISCOL2="PetalLengthCm"
IRISCOL3="PetalWidthCm"
IRISCOL4="SepalLengthCm"
IRISCOL5="SepalWidthCm"
IRISCOL6="Species"
RESULTSTABLE="results"
RESULTSCOLLIST=['Id', 'PetalLengthCm', 'PetalWidthCm', 'SepalLengthCm', 'SepalWidthCm','Prediction']
RESULTSCOL1="Id"
RESULTSCOL2="PetalLengthCm"
RESULTSCOL3="PetalWidthCm"
RESULTSCOL4="SepalLengthCm"
RESULTSCOL5="SepalWidthCm"
RESULTSCOL6="Prediction"
INICODE="""

<div>
<!-- Button trigger modal -->
<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModal">
Confirmación
</button>

<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
<div class="modal-dialog" role="document">
<div class="modal-content">
<div class="modal-header">
  <h5 class="modal-title" id="exampleModalLabel">Confirmación!</h5>
  <button type="button" class="close" data-dismiss="modal" aria-label="Close">
    <span aria-hidden="true">&times;</span>
  </button>
</div>
<div class="modal-body">
  <div class="container">
<form class="form-horizontal" action="/">
<div class="form-group">
<label class="modal-body" for="frase"><h2>¿Seguro?</h2></label>
<div class="modal-body">
  <label class="modal-body" for="frase">Va a borrar la tabla Iris!</label>
</div>
</div>
</form>
</div>
</div>
<div class="modal-footer">
  <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
  <button type="button" class="btn btn-primary">Save changes</button>
</div>
</div>
</div>
</div>
</div>
"""