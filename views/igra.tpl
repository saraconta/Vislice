% import model

%rebase('base.tpl')

  <h1>Vislice</h1>

  <blockquote>
    Vislice so najboljša igra za preganjanje dolgčasa (poleg tetrisa).
    <small>Študentje</small>
  </blockquote>

<h2>{{igra.pravilni_del_gesla()}}</h2>

<p>Nepravilni ugibi: <b>{{igra.nepravilni_ugibi()}}</b></p>

  <img src="/img/{{igra.stevilo_napak()}}.jpg" alt="obesanje">

% if stanje == model.ZMAGA:

  <h1>ZMAGA</h1>

  <form action="/nova-igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

% elif stanje == model.PORAZ:

  <h1>PORAZ</h1>
  <p>Pravilno geslo: <b>{{igra.geslo}}</b></p>
  <form action="/nova-igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

% else:

  <form action="/igra/" method="post">
   <p>Črka:<input type="text" name="crka" /></p>
   <button type="submit">Ugibaj</button>
  </form>
% end
