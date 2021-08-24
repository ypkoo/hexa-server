aws ecr get-login-password --region ap-northeast-2 | docker login --username AWS --password-stdin 749960970623.dkr.ecr.ap-northeast-2.amazonaws.com
docker build -t 749960970623.dkr.ecr.ap-northeast-2.amazonaws.com/hexa-server-nginx .
docker push 749960970623.dkr.ecr.ap-northeast-2.amazonaws.com/hexa-server-nginx