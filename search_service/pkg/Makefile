ROOTDIR         := $(shell pwd)
include $(ROOTDIR)/params

BASE_DIR        := $(ROOTDIR)/../
SRC_DIR_PATH         := $(ROOTDIR)/../src
DATABSE_DIR_PATH     := $(ROOTDIR)/../database
IMG_PATH        := $(ROOTDIR)/build_docker/demo.img

docker: $(IMG_PATH)

COPY_FILES:
	cp -R $(SRC_DIR_PATH) $(DATABSE_DIR_PATH) .

$(IMG_PATH): COPY_FILES
	sudo docker build -t $(image_name):$(version) $(ROOTDIR)

clean:
	sudo docker rmi $(image_name):$(version)
	rm -rf src database
