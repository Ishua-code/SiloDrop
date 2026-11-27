FROM public.ecr.aws/lambda/python:3.13.2026.09.28.23

RUN dnf install -y clamav1.4 clamav1.4-freshclam && dnf clean all

RUN freshclam

COPY app.py ${LAMBDA_TASK_ROOT}
CMD ["app.lambda_handler"]