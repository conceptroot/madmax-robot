echo "============================================="
echo "Detecting all i2c devices, connected to robot"
echo "============================================="
i2cdetect -y 1
echo "Now, you should insert all device addresses in settings.yaml"
