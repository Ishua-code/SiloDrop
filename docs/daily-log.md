Date         | Finished      |  What broke   | What I learned  |

25/11/2026   |Created silodrop-dev user, setup budget, set region to mumbai, and creted repo    |  the cost already gave the alert because for clg work i already used some   |   about the IAM, billing and how to select a region by the factors   |

25/11/2026  | Created a S3 bucket and added files in it | ntg broked | I learnt about S3, how it works and the object URL, the predigned URL and the prefixes |

25/11/26   | Created a lambda function | Deployed a lambda_handler.py in code and tested| The init duration--cold start for setup | Learnt the code and test, the logs--cloudWatch, the permission poliies(what is allowed to do), the trust policies(who is allowed to do) , sts-Security service token----provide the temporary role  |

26/11/2026   | Created the IAM-inline policy and the lambda function for presigned URL | I copied the slash (the escape character of json) nd  it failed | I learnt abt the inline policies, the handlers, the boto3--(aws python library), and experimented how the link works by removing the inline policies, by changing the role's resource and tried uploading after the expiry time

