FROM python:3
COPY src/ /src
COPY database/ /database
RUN echo '#!/bin/bash' > /usr/bin/entrypoint.sh \
    && echo 'python /src/Infoblox_utility.py $@' >> /usr/bin/entrypoint.sh \
    && chmod +x /usr/bin/entrypoint.sh

ENTRYPOINT ["/usr/bin/entrypoint.sh"]