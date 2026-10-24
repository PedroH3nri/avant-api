// Pipeline do avant-api no Jenkins: checagens, imagem no GHCR e deploy (develop em staging,
// main em produção). Tudo vem da biblioteca em avant-infra/jenkins (ver o README de lá).
@Library('avant') _

avantPipeline(service: 'api', checks: 'python')
