
import socket
import telnetlib


s = socket.socket()
s.connect(("itsec.sec.in.tum.de", 7025))
# Chosen Plaintext Attack on RSA
# idea https://crypto.stackexchange.com/questions/2323/how-does-a-chosen-plaintext-attack-on-rsa-work

n = 31511564540733510745119160555849790586658736078995926138938535802938687308372270495817783933340060681773033322388651205126697332436106943823768892885824384816616707561073010507264693221167953982741722947421173352096779833391716248640759214437975808719610239896720756762152382233956921377862900844373271271633441224605191962708005539801818821038150900437910524787374195607458725771735840356530155558119951348786334434374051473655235808803885460360983745083039054245376435787478073833501446705665139014671301534356862915478678476632672633176304226010163232805220740485841258380224994639873580833185794681663032400599777
e = 65537
# The GCHQ sniffed this RSA-encrypted message from my friend to me today: 7a259c81376119e8b9e028e963a3f09799d0dc7ca60f3f4751aeee16c24990748f0dab0a435b11c93ad107a1d85d861a19123308e8f109f9c50e835f900471c0e786d79f7097a522f66b510212c3c0643aa03290707a9a77a97dcfbf2e9a80bca1ed2cd006504ae7032b8ab62f7ba84063edcc68ef088e30eeb5f3934e311b4bb3f7a446aa0084ca9f6f9f7d96b243164dabc2a0a33c8f9a269f8db092e0b816468ff4ffa433253f904e13e5ae1a42dcc583abf1f6874fb0df228107c8983143fcfe4b197a6a60a5cce6a3b4be7c93d8b9c9d5b7261efa0e22562235073737eb23179646ccb72b0b61415044819565032ed9cd76a00329f55c2d793df6bb136f
c = "7a259c81376119e8b9e028e963a3f09799d0dc7ca60f3f4751aeee16c24990748f0dab0a435b11c93ad107a1d85d861a19123308e8f109f9c50e835f900471c0e786d79f7097a522f66b510212c3c0643aa03290707a9a77a97dcfbf2e9a80bca1ed2cd006504ae7032b8ab62f7ba84063edcc68ef088e30eeb5f3934e311b4bb3f7a446aa0084ca9f6f9f7d96b243164dabc2a0a33c8f9a269f8db092e0b816468ff4ffa433253f904e13e5ae1a42dcc583abf1f6874fb0df228107c8983143fcfe4b197a6a60a5cce6a3b4be7c93d8b9c9d5b7261efa0e22562235073737eb23179646ccb72b0b61415044819565032ed9cd76a00329f55c2d793df6bb136f"

c_a = (int.from_bytes(bytes.fromhex(c), byteorder="little") * pow(2,e,n)) % n
# c_a: d8f5fb3817e2f004005ce9a3c98f435a5497ca08cec52ca99419b6ccb3ed133ad34d9f483b2368201d31f4fd7369a8f4571b122834e388fefca7708956db4c136dcba4cfac1ea6cdeaf3b600b4965f458cc5d7a40656675718a6c8f4bcb739445aefdd00fc0386da4a8296c699305e6cf0ed233ff7972708e49b6f9aa3e452bd308b2fd1e50be3af15fc627e9ba969a7aa8430f2e3f26be3764856ebe2ecd6bd4555b0c56eeec689747a78265a00a61266b4a517e3de44936f42b566717e69e2bbd4b3f695ae9d022de37dd3383e249eb046599bf94721284f8c338fc434f0bad7f8acfdbda4f217737359b18125d2140486cd66ccb0259ec41baf16a7ab815b

bca = c_a.to_bytes(length=2048//8, byteorder="little")
print(bca.hex().encode())
# 5b81aba716af1bc49e25b0cc66cd860414d22581b159737317f2a4bdfdacf8d7baf034c48f338c4f282147f99b5946b09e243e38d37de32d029dae95f6b3d4bbe2697e7166b5426f9344dee317a5b46612a6005a26787a7489c6ee6ec5b05545bdd6ece2eb564876e36bf2e3f23084aaa769a99b7e62fc15afe30be5d12f8b30bd52e4a39a6f9be4082797f73f23edf06c5e3099c696824ada8603fc00ddef5a4439b7bcf4c8a61857675606a4d7c58c455f96b400b6f3eacda61eaccfa4cb6d134cdb568970a7fcfe88e33428121b57f4a86973fdf4311d2068233b489f4dd33a13edb3ccb61994a92cc5ce08ca97545a438fc9a3e95c0004f0e21738fbf5d8

# --> an den server schicken und auf rückgabe warten

# The decrypted message is (in hex): ccd8c2cef672c66e72686066cc6e7060c4606cc462c2cc72726270cc686a66c8c460646c66686864cafa14000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000*** Connection closed by remote host ***
# Mit Rückgabe weiter machen
rt = "ccd8c2cef672c66e72686066cc6e7060c4606cc462c2cc72726270cc686a66c8c460646c66686864cafa14000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"


# Extended Euclidean Algorithm verwenden
# from https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
def extended_gcd(a, b):
    old_r, r = a,b
    old_s, s = 1 ,0
    old_t, t = 0,1

    while r!=0:
        quotient = old_r // r
        old_r, r = r,old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_s,old_t


x, y = extended_gcd(2,n)
m2 = (int(rt,16) * (x%n))%n

# Ausgeben
print(bytes.fromhex(hex(m2)[2:]).decode(errors="ignore"))


t = telnetlib.Telnet()
t.sock = s
t.interact()
