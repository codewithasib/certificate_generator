from certificate_generator import CertificateGenerator

template_path = r'certificate_generator/src/template2.png'
font_path = r'certificate_generator/src/GreatVibes-Regular.ttf'
logo_path = r'certificate_generator/src/logo.png'

generator = CertificateGenerator(template_path, font_path, logo_path, font_size=360)


def main():
    names = ['Certificate Generator']
    for name in names:
        generator.create_certificate(name)
    print(len(names), "certificates done.")


if __name__ == '__main__':
    main()
