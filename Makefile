
build_app_packages:
	docker build -t mwaaas/dg:$(v) devops/dg_packages

push_app_packages:
	docker push mwaaas/dg:$(v)

build_push_app_packages: build_app_packages push_app_packages

deploy:
	docker-compose stop web
	docker-compose rm -f web
	docker-compose build
	docker-compose up