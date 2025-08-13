document.addEventListener('DOMContentLoaded', function () {
  var elems = document.querySelectorAll('.sidenav');
  M.Sidenav.init(elems);
  var collapses = document.querySelectorAll('.collapsible');
  M.Collapsible.init(collapses);
});
