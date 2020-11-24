import re


class CalcIPv4:
    def __init__(self, ip, mask=None, prefix=None):
        self.ip = ip
        self.mask = mask
        self.prefix = prefix

        self._set_broadcast()
        self._set_rede()


    @property
    def rede(self):
        return self._rede

    @property
    def broadcast(self):
        return self._broadcast

    @property
    def ips(self):
        return self._get_ips()

    @property
    def ip(self):
        return self._ip

    @property
    def mask(self):
        return self._mask

    @property
    def prefix(self):
        return self._prefix

    @ip.setter
    def ip(self, value):
        if not self._validate_ip(value):
            raise ValueError("Invalid IP")

        self._ip = value
        self._ip_bin = self._ip_to_bin(value)

    @mask.setter
    def mask(self, value):
        if not value:
            return

        if not self._validate_ip(value):
            raise ValueError("Invalid MASK")

        self._mask = value
        self._mask_bin = self._ip_to_bin(value)

        if not hasattr(self, "prefix"):
            self.prefix = self._mask_bin.count("1")

    @prefix.setter
    def prefix(self, value):
        if not value:
            return

        if not isinstance(value, int):
            raise TypeError("Prefix must be integer")

        if value > 32:
            raise TypeError("Prefix must be 32Bits")

        self._prefix = value
        self._mask_bin = (value * "1").ljust(32, "0")

        if not hasattr(self, "mask"):
            self.mask = self._bin_to_ip(self._mask_bin)

    @staticmethod
    def _validate_ip(ip):
        regexp = re.compile(r"^([0-9]){1,3}.([0-9]){1,3}.([0-9]){1,3}.([0-9]){1,3}$")

        if regexp.search(ip):
            return True

    @staticmethod
    def _ip_to_bin(ip):
        blocks = ip.split(".")
        blocks_bin = [bin(int(x))[2:].zfill(8) for x in blocks]
        return "".join(blocks_bin)

    @staticmethod
    def _bin_to_ip(ip):
        n = 8
        blocks = [str(int(ip[i : n + i], 2)) for i in range(0, 32, n)]
        return ".".join(blocks)

    def _set_broadcast(self):
        host_bits = 32 - self.prefix
        self._broadcast_bin = self._ip_bin[: self.prefix] + (host_bits * "1")
        self._broadcast = self._bin_to_ip(self._broadcast_bin)
        return self._broadcast

    def _set_rede(self):
        host_bits = 32 - self.prefix
        self._rede_bin = self._ip_bin[: self.prefix] + (host_bits * "0")
        self._rede = self._bin_to_ip(self._rede_bin)
        return self._rede

    def _get_ips(self):
        return 2 ** (32 - self.prefix)
