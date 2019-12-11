// initialize variables
var doc = app.activeDocument;
var backdropChoice = confirm("Does this photo contain an incomplete backdrop?");

// set up before performing functions
doc.activeLayer = doc.layers[0];
doc.layers[0].visible = false;
doc.layers[1].visible = true;
try {
    doc.rasterizeAllLayers();
}
catch(error) {
    // do nothing
}

// cut person and paste into new layer
app.doAction("selectPersonMask", "myActions.ATN");
doc.selection.feather(50);
doc.selection.expand(300);
app.doAction("layerSelection", "myActions.ATN");

doc.layers[1].remove();

//set background layer as active layer
doc.activeLayer = doc.layers[1];

// make first layer invisible
doc.layers[0].visible = false;

// get of person mask
app.doAction("selectPersonMask", "myActions.ATN");

// expand selection and remove person space
doc.selection.expand(300);
app.doAction("contentAware", "myActions.ATN");

// deselect and apply blur to remove backdrop wrinkles
doc.selection.deselect();
doc.artLayers[1].applyGaussianBlur(100);

if (backdropChoice) {
    // select inverse of red backdrop
    app.doAction("selectRedBackdrop", "myActions.ATN");
    app.doAction("makeSelectionHard", "myActions.ATN");
    doc.selection.invert();
    doc.selection.expand(750);

    // fill backdrop
    app.doAction("contentAware", "myActions.ATN");
    doc.selection.deselect();
    doc.artLayers[1].applyGaussianBlur(200);
}

// make first layer visible again
doc.layers[0].visible = true;