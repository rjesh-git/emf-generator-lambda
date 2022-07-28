
# EMF Generator Lambda

A Lambda which generates custom metrics by using embedded metric format logs to CloudWatch.


## Deployment

To deploy this project run the below,
**and make sure to run docker daemon, which required for this module to package the layer.**

```bash
  pip install -r requirements.txt
  cdk synth
  cdk deploy
```


## Support

It's an experimental feature only to be used in PoC and not for production use, refer to https://docs.aws.amazon.com/cdk/api/v2/docs/aws-lambda-python-alpha-readme.html for public release of this module.

## License

[MIT](https://choosealicense.com/licenses/mit/)


