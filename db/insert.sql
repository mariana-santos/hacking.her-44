-- Inserindo tipos de quiz
INSERT INTO quiztype VALUES (1, "Simples", "Você descobrirá se a tecnologia é um caminho para você. Vamos entender suas habilidades e facilitar o caminho!", "simple");

INSERT INTO quiztype VALUES (2, "Avançado", "Já tendo decidido na área de tecnologia, vamos te ajudar a encontrar a área específica que combine mais com você!", "advanced");


-- Inserindo enquetes
INSERT INTO quiz VALUES (1, "Será que a tecnologia é pra mim?", "Com essa enquete você vai responder perguntas básicas a fim de saber se a tecnologia se encaixa nos seus interesses", 1);

INSERT INTO quiz VALUES (2, "Data Science, desenvolvimento... Qual a diferença? Qual devo seguir?", "Responda as simples perguntas e descubra as áreas que fazem mais sentido com a sua personalidade! Além disso ao fim vamos te direcionar com cursos direcionados às suas necessidades!", 2);


-- Inserindo perguntas
INSERT INTO question (id, title, description, id_image, id_quiz) VALUES 
(1, 'Qual era (ou é) sua matéria favorita na escola?', 'Pense nas matérias que você já estudou e escolha a que você mais gostava e/ou tinha facilidade.', null, 1),
(2, 'Você gosta de resolver problemas lógicos?', 'Pense em atividades como resolver quebra-cabeças, jogos de lógica, sudoku, etc.', null, 1),
(3, 'Você prefere trabalhar em grupo ou sozinho?', 'Considere sua preferência em termos de produtividade e conforto.', null, 1),
(4, 'Você se considera uma pessoa criativa?', 'Pense em como você lida com tarefas que exigem inovação e pensamento fora da caixa.', null, 1),
(5, 'Para você, como seria um dia ideal de diversão?', 'Pense no que você gostaria de fazer em um dia livre.', null, 1);

-- Inserindo opções
INSERT INTO question_option (id, description, points, id_image, id_question) VALUES 

-- Pergunta 1
(1, 'Matemática', 3, null, 1),
(2, 'Ciências', 2, null, 1),
(3, 'Língua Portuguesa', 1, null, 1),

-- Pergunta 2
(4, 'Sim, eu adoro', 3, null, 2),
(5, 'Não, prefiro atividades mais práticas', 1, null, 2),
(6, 'Às vezes, depende do problema', 2, null, 2),

-- Pergunta 3
(7, 'Prefiro trabalhar sozinha', 3, null, 3),
(8, 'Prefiro trabalhar em grupo', 2, null, 3),
(9, 'Não tenho preferência', 1, null, 3),

-- Pergunta 4
(10, 'Sim, muito criativa', 4, null, 4),
(11, 'Um pouco, depende da tarefa', 2, null, 4),
(12, 'Não, sigo mais regras', 1, null, 4),

-- Pergunta 5
(15, 'Aprendendo coisas novas', 5, null, 5),
(16, 'No parque ou praticando atividades físicas', 2, null, 5),
(17, 'Jogando jogos on-line com os meus amigos', 4, null, 5);

-- Inserindo opções de carreira
INSERT INTO career_option (id, title, description, id_image) VALUES 
(1, 'Deu match! Você pode ser uma ótima profissional da tecnologia', 'Você tem habilidades lógicas e matemáticas, o que é ótimo para carreiras na área. Que tal agora fazer a enquete avançada para saber seus próximos passos?', null),
(2, 'Opa! Baseado nas suas respostas, você se daria melhor em outras áreas do conhecimento', 'Você se daria bem em áreas que envolvem mais interação humana e criatividade. Quer voltar e escolher outro teste?', null),

INSERT INTO result (id, id_quiz, min_points, max_points, id_career_option) VALUES 
(1, 1, 1, 9, 1),
(2, 1, 10, 20, 2),

INSERT INTO course (id, title, description, link, image, id_career_option) VALUES 
(1, 'Informática Essencial: Windows e Office', 'Você aprenderá a usar aplicativos do Microsoft Office para editar textos, criar apresentações e planilhas, além de trabalhar com pastas no Windows e navegar na internet com segurança.', 'https://www.sp.senac.br/cursos-livres/curso-de-informatica-essencial-windows-e-office', null, 1),
(2, 'Técnico em Desenvolvimento de Sistemas', 'Você aprenderá a fazer análise e desenvolvimento de sistemas em diferentes plataformas, programar aplicativos, realizar testes e a manutenção da estrutura de banco de dados.', 'https://www.sp.senac.br/cursos-tecnicos/curso-tecnico-em-desenvolvimento-de-sistemas', null, 1),

(3, 'Fotografia: composição e linguagem', 'Você aprenderá a usar técnicas e recursos para produzir ensaios fotográficos de qualidade, além de pesquisar referências e linguagens de fotografia para construir seu repertório.', 'https://www.sp.senac.br/cursos-livres/curso-de-fotografia-composicao-e-linguagem', null, 2),
(4, 'Desenho Técnico', 'Você aprenderá a fazer desenhos técnicos manualmente para projetos de arquitetura, engenharia, design de interiores e de produto.', 'https://www.sp.senac.br/cursos-livres/curso-de-desenho-tecnico', null, 2);

-- Quiz avançado
INSERT INTO question VALUES (6, "Você gosta de lidar com grandes volumes de dados?", "Isso pode incluir lidar com padrões de dados, modificação, limpeza de dados...", null, 2);
INSERT INTO question VALUES (7, "Você prefere trabalhar em tarefas que envolvam design e criatividade?", "Considere atividades que exigem inovação e pensamento visual.", null, 2);
INSERT INTO question VALUES (8, "Você se interessa por infraestrutura e como os sistemas funcionam em segundo plano?", "Pense em atividades relacionadas à administração de sistemas e redes.", null, 2);
INSERT INTO question VALUES (9, "Você se sente confortável mexendo com peças de eletrônicos ou mantendo qualquer tipo de eletrônico?", "Considere a instalação, reparo e manutenção de coisas do seu dia-a-dia.", null, 2);
INSERT INTO question VALUES (10, "Você gosta de desenvolver aplicações e solucionar problemas de lógica complexa?", "Pense em atividades de programação e desenvolvimento de software.", null, 2);

INSERT INTO question_option (description, points, id_question) VALUES 
("Sim, gosto muito", 3, 6),
("Gosto às vezes", 2, 6),
("Indiferente", 1, 6),
("Não gosto", 0, 6);

INSERT INTO question_option (description, points, id_question) VALUES 
("Sim, gosto muito", 3, 7),
("Gosto às vezes", 2, 7),
("Indiferente", 1, 7),
("Não gosto", 0, 7);

INSERT INTO question_option (description, points, id_question) VALUES 
("Sim, gosto muito", 3, 8),
("Gosto às vezes", 2, 8),
("Indiferente", 1, 8),
("Não gosto", 0, 8);

INSERT INTO question_option (description, points, id_question) VALUES 
("Sim, gosto muito", 3, 9),
("Gosto às vezes", 2, 9),
("Indiferente", 1, 9),
("Não gosto", 0, 9);

INSERT INTO question_option (description, points, id_question) VALUES 
("Sim, gosto muito", 3, 10),
("Gosto às vezes", 2, 10),
("Indiferente", 1, 10),
("Não gosto", 0, 10);

INSERT INTO career_option (title, description, id_image) VALUES
("DevOps ou Redes", "Ótimo resultado! É uma área ampla com atuação em infraestrutura de TI, automação de processos e gerenciamento de redes.", NULL),
("DBA ou Data Science", "Você nasceu para os dados! Essa área atua com a administração de bancos de dados ou análise de dados para tomada de decisões.", NULL),
("Manutenção ou Hardware", "Você prefere a mão na massa! Nessa área as funções incluem a manutenção e suporte técnico de hardware de computadores e periféricos.", NULL),
("Designer/UX ou Desenvolvedor Front-End", "Você é criativo! Combina com design de interfaces de usuário ou desenvolvimento de aplicações web.", NULL),
("Desenvolvedor Back-End", "Seu perfil é lógico! Procure sobre desenvolvimento de sistemas e lógica de funcionamento de aplicações.", NULL);

select * from career_option;

INSERT INTO result (min_points, max_points, id_quiz, id_career_option) VALUES 
(1, 6, 2, 3),  -- DevOps ou Redes
(7, 12, 2, 4), -- DBA ou Data Science
(13, 18, 2, 5), -- Manutenção ou Hardware
(19, 24, 2, 6), -- Designer/UX ou Desenvolvedor Front-End
(25, 30, 2, 7); -- Desenvolvedor Back-End


INSERT INTO course (title, description, link, image, id_career_option) VALUES 
('Administrador de Redes', 'Você aprenderá a planejar e a realizar manutenção em redes de computadores, instalar, configurar e gerenciar sistemas, prestando suporte e implementando políticas de segurança.', 'https://www.sp.senac.br/cursos-livres/curso-de-administrador-de-redes', null, 3),
('Amazon AWS Cloud Practitioner - básico para a certificação', 'Você aprenderá a implementar, gerenciar e monitorar serviços em nuvem, adquirindo conhecimentos básicos para os testes de certificação AWS Cloud Practitioner.', 'https://www.sp.senac.br/cursos-livres/curso-de-amazon-aws-cloud-practitioner-basico-para-a-certificacao', null, 3),

('Administrador de Banco de Dados', 'Você aprenderá a implementar, instalar, configurar, administrar e realizar procedimentos de otimização e manutenção do sistema de banco de dados, além de monitorar e implantar rotinas de backup e plano de restauração.', 'https://www.sp.senac.br/cursos-livres/curso-de-administrador-de-banco-de-dados', null, 4),
('Ensino Médio Técnico em Ciências de Dados', 'Você estudará linguagens, matemática, ciências da natureza e suas tecnologias, além de ciências humanas e sociais aplicadas.', 'https://www.sp.senac.br/ensino-medio-tecnico/ensino-medio-tecnico-em-ciencias-de-dados', null, 4),

('Formação em Hardware', 'Você aprenderá a configurar e a fazer a manutenção de impressoras, rede local e computadores executando tarefas, como limpar, reparar, montar e desmontar os componentes.', 'https://www.sp.senac.br/cursos-livres/curso-de-formacao-em-hardware', null, 5),
('Manutenção de Microcomputadores', 'Você aprenderá a planejar e a executar montagem e manutenção de computadores seguindo as recomendações técnicas, além de configurar sistema operacional e realizar teste e inspeção.', 'https://www.sp.senac.br/cursos-livres/curso-de-manutencao-de-microcomputadores', null, 5),

('Desenvolvedor Web Front-end 1: HTML e CSS', 'Você aprenderá a planejar e desenvolver sites responsivos com imagens, linguagem de marcação HTML5, estilos CSS3 e conceitos de Web Semântica.', 'https://www.sp.senac.br/cursos-livres/curso-de-desenvolvedor-web-front-end-1-html-e-css', null, 6),
('Design', 'Que tal personalizar seus estudos de acordo com a carreira que deseja ter? Neste curso, é você quem escolhe qual área do design terá mais destaque na sua formação: gráfico, digital, produtos ou serviços.', 'https://www.sp.senac.br/graduacao/bacharelado-em-design', null, 6),

('Lógica de Programação Direcionada a PHP', 'Você aprenderá a interpretar a sintaxe e o formato da linguagem de programação PHP para criar algoritmos e desenvolver aplicações e sistemas computacionais web.', 'https://www.sp.senac.br/cursos-livres/curso-de-logica-de-programacao-direcionada-a-php', null, 7),
('Programação em C#', 'Você aprenderá executar processos de codificação em linguagem C#, utilizando classes, matrizes, programação orientada a objetos e também dados e variáveis.', 'https://www.sp.senac.br/cursos-livres/curso-de-programacao-em-c', null, 7);
