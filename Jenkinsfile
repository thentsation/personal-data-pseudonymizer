// Pipeline da plataforma (Shared Library "platform", repo devops-platform/jenkins-lib).
// PRs e branches: validação, CI (docker build --target test), pip-audit e Trivy.
// main: build e execução de teste da imagem (job que precisa terminar com exit 0), release
// (semantic-release), rebuild do portfolio e rebuild semanal. Não é serviço: sem deploy.
@Library('platform') _

appPipeline(
    name: 'personal-data-pseudonymizer',
    deployBranch: 'main',
    deploy: false,
    run: [mode: 'job'],
    notify: [[repo: 'ntsation/portfolio', event: 'rebuild']],
)
