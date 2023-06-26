var detailsElements = document.querySelectorAll('details');

detailsElements.forEach(function(details) {
  details.addEventListener('toggle', function() {
    var currentDetails = this;
    setTimeout(function() {
      if (currentDetails.open) {
        currentDetails.classList.add('reflow');
      } else {
        currentDetails.classList.remove('reflow');
      }
    }, 10);
  });
});
