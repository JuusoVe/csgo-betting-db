mkdir /etc/codedeploy-agent/

mkdir /etc/codedeploy-agent/conf

echo "in da script"

cat <<EOT >> /etc/codedeploy-agent/conf/codedeploy.onpremises.yml

---

aws_access_key_id: $replace

aws_secret_access_key: $also_replace

iam_user_arn: $and_me

region: eu-central-1

EOT

wget https://aws-codedeploy-us-west-2.s3.us-west-2.amazonaws.com/latest/install

chmod +x ./install

sudo ./install auto