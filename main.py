from adam.dme import DME

if __name__ == "__main__":
    dme = DME("./models/fw_info.bin")
    dme.load_model("./models/all_models.bin")
    dme.configure()
