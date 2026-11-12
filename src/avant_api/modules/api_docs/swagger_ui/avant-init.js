/** Inicia o Swagger UI com o OpenAPI da API, sem o validador externo do swagger.io. */
window.ui = SwaggerUIBundle({
  url: "/api/v1/openapi.json",
  dom_id: "#swagger-ui",
  validatorUrl: null,
  deepLinking: true,
  showExtensions: true,
  showCommonExtensions: true,
  presets: [SwaggerUIBundle.presets.apis, SwaggerUIBundle.SwaggerUIStandalonePreset],
  layout: "BaseLayout",
});
