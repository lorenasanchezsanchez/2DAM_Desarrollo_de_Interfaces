(() => {
  "use strict";

  const DOMINIO_PERMITIDO = "lawer.github.io";
  const RUTA_PERMITIDA = "/tutorials-pmdm/docs/compose-multiplatform/";

  function esTutorialCompose(url) {
    return (
      url.hostname === DOMINIO_PERMITIDO &&
      url.pathname.startsWith(RUTA_PERMITIDA)
    );
  }

  function mostrarTutorial(url, titulo) {
    const contenido = document.querySelector(".md-content__inner");

    if (!contenido) {
      window.location.href = url.href;
      return;
    }

    // Guarda la URL y el título para poder recuperarlos.
    history.pushState(
      { composeVisor: true, url: url.href, titulo },
      "",
      "?tutorial=" + encodeURIComponent(url.href)
    );

    // Crea el visor.
    contenido.replaceChildren();

    const encabezado = document.createElement("h1");
    encabezado.textContent = titulo || "Compose Multiplatform";

    const contenedor = document.createElement("div");
    contenedor.className = "compose-visor";

    const iframe = document.createElement("iframe");
    iframe.src = url.href;
    iframe.title = titulo || "Tutorial de Compose Multiplatform";
    iframe.loading = "eager";
    iframe.referrerPolicy = "strict-origin-when-cross-origin";

    contenedor.appendChild(iframe);
    contenido.append(encabezado, contenedor);

    window.scrollTo({ top: 0, behavior: "auto" });
  }

  // Intercepta los enlaces de los tutoriales.
  document.addEventListener("click", (evento) => {
    const enlace = evento.target.closest("a");

    if (!enlace || evento.defaultPrevented) return;
    if (evento.button !== 0) return;
    if (evento.ctrlKey || evento.metaKey || evento.shiftKey || evento.altKey) return;
    if (enlace.target === "_blank") return;

    let url;

    try {
      url = new URL(enlace.href);
    } catch {
      return;
    }

    if (!esTutorialCompose(url)) return;

    evento.preventDefault();

    const titulo = enlace.textContent.trim();

    mostrarTutorial(url, titulo);
  });

  // Recupera el tutorial al usar Atrás o Adelante.
  window.addEventListener("popstate", (evento) => {
    if (evento.state?.composeVisor && evento.state.url) {
      mostrarTutorialSinHistorial(
        evento.state.url,
        evento.state.titulo
      );
    } else {
      window.location.reload();
    }
  });

  function mostrarTutorialSinHistorial(urlTexto, titulo) {
    const contenido = document.querySelector(".md-content__inner");
    if (!contenido) return;

    const url = new URL(urlTexto);

    if (!esTutorialCompose(url)) return;

    contenido.replaceChildren();

    const encabezado = document.createElement("h1");
    encabezado.textContent = titulo || "Compose Multiplatform";

    const contenedor = document.createElement("div");
    contenedor.className = "compose-visor";

    const iframe = document.createElement("iframe");
    iframe.src = url.href;
    iframe.title = titulo || "Tutorial de Compose Multiplatform";

    contenedor.appendChild(iframe);
    contenido.append(encabezado, contenedor);
  }
})();