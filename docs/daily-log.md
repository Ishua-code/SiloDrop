Date         | Finished      |  What broke   | What I learned  |

25/11/2026   |Created silodrop-dev user, setup budget, set region to mumbai, and creted repo    |  the cost already gave the alert because for clg work i already used some   |   about the IAM, billing and how to select a region by the factors   |

25/11/2026  | Created a S3 bucket and added files in it | ntg broked | I learnt about S3, how it works and the object URL, the predigned URL and the prefixes |

25/11/26   | Created a lambda function | Deployed a lambda_handler.py in code and tested| The init duration--cold start for setup | Learnt the code and test, the logs--cloudWatch, the permission poliies(what is allowed to do), the trust policies(who is allowed to do) , sts-Security service token----provide the temporary role  |

26/11/2026   | Created the IAM-inline policy and the lambda function for presigned URL | I copied the slash (the escape character of json) nd  it failed | I learnt abt the inline policies, the handlers, the boto3--(aws python library), and experimented how the link works by removing the inline policies, by changing the role's resource and tried uploading after the expiry time

26/11/2026   | Created the sqs service, the s3 event notifier and the processor handler, a new role for sqs | ntg broke | When uploaded to S3 the s3 event notifier successfully sent the notification to sqs, and the processor works and send it to the sqs and sqs to lambda

26/11/20226   | Created a dynamoDB and the inline poilicy  for it and the processor lambda_handler(updated version) | When i detached inline policy i thought the upload itself will not happen , but i was wrong the upload happend because of the pre-signed url and ntg to do with inline ddb policy, we cloud watch that only in cloudWatch  | I learnt the dynamoDB, its features and the inline policy for this  

27/11/2026    | Created the ECR, and dockerfile and the lambda using the container image | went through many breaks such as docker port i gave wrong....was not in the right dir (small mistakes) and the media type error ---becouse of the logs while building (Rebuilt with --provenance=false and pushed again) | I learnt abt the docker file, image, container, the ECR 