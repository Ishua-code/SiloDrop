The Region----I picked Mumbai rather than Hyderabad, because of factors such as Latency (not much diff for documents), data residency (the laws of the country both India only so no problem), Service region (Mumbai is more service mature than Hyderabad), cost (more or less same) and the tutorials most use Mumbai(so easy to refer)

The Bucket---Should stay private as we use customers sensitive data(no public access)
Use the trailing salshes properly----later used for String Matching.

Direct-to-S3 upload with presigned URLs. Files never pass through our code.

SQS between S3 and Lambda: buffering, retries, and a place for failures (DLQ comes in Week 3).

Tenant comes from the object key, not from anything the client claims.

Partition key tenant_id, sort key object_key. Rejected: timestamp-based sort key. Trade-off: one very large tenant concentrates traffic.

On-demand DynamoDB instead of provisioned, because idle cost is zero.

Separate role per function, each with only the actions it needs. Rejected: reusing one broad role.

A separate silodrop-cli user for pushing images, limited to ECR repositories named silodrop-*. One documented exception: ecr:GetAuthorizationToken can't be limited to a resource.

Container image (not zip) for ClamAV, because of its size. Practised with a tiny image first.