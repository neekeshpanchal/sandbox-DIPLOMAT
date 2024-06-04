<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DIPLOMAT - Deep Learning-Based Identity Preserving Labeled-Object Multi-Animal Tracking</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        header {
            background: #333;
            color: #fff;
            padding: 1rem 0;
            text-align: center;
        }
        .container {
            max-width: 1200px;
            margin: auto;
            overflow: hidden;
            padding: 0 2rem;
        }
        h1, h2, h3 {
            color: #333;
        }
        p {
            color: #666;
        }
        .video, .images, .ui-demo {
            display: flex;
            justify-content: center;
            margin: 2rem 0;
        }
        .video iframe, .images img, .ui-demo img {
            max-width: 100%;
            height: auto;
        }
        .commands {
            background: #fff;
            padding: 1rem;
            margin: 1rem 0;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .commands pre {
            background: #f4f4f4;
            padding: 1rem;
            border-radius: 5px;
        }
        .author-contact {
            margin: 2rem 0;
            text-align: center;
        }
        footer {
            background: #333;
            color: #fff;
            text-align: center;
            padding: 1rem 0;
            margin-top: 2rem;
        }
    </style>
</head>
<body>
    <header>
        <h1>DIPLOMAT</h1>
        <p>Deep Learning-Based Identity Preserving Labeled-Object Multi-Animal Tracking</p>
        <p><strong>NOTE:</strong> DIPLOMAT is currently alpha software, there may be minor bugs and usability issues.</p>
    </header>

    <div class="container">
        <section>
            <h2>About</h2>
            <p>DIPLOMAT provides algorithms and tools for performing multi-animal identity preserving tracking on top of single animal and multi animal CNN based tracking packages. Currently, it supports running on both DeepLabCut and SLEAP projects. Unlike other multi-animal tracking packages, DIPLOMAT's algorithms work directly off confidence maps instead of running peak detection, allowing for more nuanced tracking results compared to other methods.</p>
            
            <div class="video">
                <video controls>
                    <source src="https://github.com/TravisWheelerLab/DIPLOMAT/assets/47544550/d805b673-4678-4297-b288-3fd08ad3cf62.mp4" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
            </div>

            <div class="images">
                <img src="https://raw.githubusercontent.com/TravisWheelerLab/DIPLOMAT/main/docs/source/_static/imgs/example1.png" alt="Example of tracking 2 Degus in a Box">
                <img src="https://raw.githubusercontent.com/TravisWheelerLab/DIPLOMAT/main/docs/source/_static/imgs/example2.png" alt="Example of tracking 3 Rats">
            </div>

            <div class="ui-demo">
                <img src="https://raw.githubusercontent.com/TravisWheelerLab/DIPLOMAT/main/docs/source/_static/imgs/UIDemo.png" alt="UI Demo Showing user correcting tracking in a video">
            </div>
        </section>

        <section>
            <h2>Installation</h2>
            <p>DIPLOMAT includes four environment configuration files for setting up DIPLOMAT with <a href="https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html" target="_blank">mamba</a>, which can be installed on Windows, Linux, or MacOS using the <a href="https://github.com/conda-forge/miniforge" target="_blank">Miniforge</a> installer.</p>
            <p>To create an environment using mamba, run one of these four commands:</p>
            <div class="commands">
                <pre># Create the environment for using DIPLOMAT with DeepLabCut
# GPU:
mamba env create -f https://raw.githubusercontent.com/TravisWheelerLab/DIPLOMAT/main/conda-environments/DIPLOMAT-DEEPLABCUT.yaml
# CPU only:
mamba env create -f https://raw.githubusercontent.com/TravisWheelerLab/DIPLOMAT/main/conda-environments/DIPLOMAT-DEEPLABCUT-CPU.yaml
# OR Create an environment for using DIPLOMAT with SLEAP instead...
# GPU:
mamba env create -f https://raw.githubusercontent.com/TravisWheelerLab/DIPLOMAT/main/conda-environments/DIPLOMAT-SLEAP.yaml
# CPU only:
mamba env create -f https://raw.githubusercontent.com/TravisWheelerLab/DIPLOMAT/main/conda-environments/DIPLOMAT-SLEAP-CPU.yaml</pre>
            </div>
            <p>And then activate the environment with one of these two commands:</p>
            <div class="commands">
                <pre># Activate the DeepLabCut/DIPLOMAT environment...
mamba activate DIPLOMAT-DEEPLABCUT
# Activate the SLEAP/DIPLOMAT environment...
mamba activate DIPLOMAT-SLEAP</pre>
            </div>
            <p>For a more thorough explanation of the installation process and alternative installation methods, see the <a href="https://diplomat.readthedocs.io/en/latest/installation.html" target="_blank">documentation</a>.</p>
        </section>

        <section>
            <h2>Usage</h2>
            <h3>Running DIPLOMAT</h3>
            <p>To run DIPLOMAT on a video once it is installed, simply use DIPLOMAT's <code>unsupervised</code> and <code>supervised</code> commands to track a video:</p>
            <div class="commands">
                <pre># Run DIPLOMAT with no UI...
diplomat track -c path/to/config -v path/to/video
# Run DIPLOMAT with UI...
diplomat track_and_interact -c path/to/config -v path/to/video</pre>
            </div>
            <p>Multiple videos can be tracked by passing them as a list:</p>
            <div class="commands">
                <pre>diplomat track -c path/to/config -v [path/to/video1, path/to/video2, "path/to/video3"]</pre>
            </div>
            <p>Once tracking is done, DIPLOMAT can create labeled videos via its <code>annotate</code> subcommand:</p>
            <div class="commands">
                <pre>diplomat annotate -c path/to/config -v path/to/video</pre>
            </div>
            <p>If you need to reopen the UI to make further major modifications, you can do so using the <code>interact</code> subcommand:</p>
            <div class="commands">
                <pre>diplomat interact -s path/to/ui_state.dipui</pre>
            </div>
            <p>This displays the full UI again for making further edits. Results are saved back to the same files.</p>
            <p>If you need to make minor modifications after tracking a video, you can do so using the <code>tweak</code> subcommand:</p>
            <div class="commands">
                <pre>diplomat tweak -c path/to/config -v path/to/video</pre>
            </div>
            <p>This will display a stripped down version of the interactive editing UI, allowing for minor tweaks to be made to the tracks, and then saved back to the same file.</p>
            <p>For a list of additional ways DIPLOMAT can be used, see the <a href="https://diplomat.readthedocs.io/en/latest/basic_usage.html" target="_blank">documentation</a>.</p>

            <h3>Additional Help</h3>
            <p>All DIPLOMAT commands are documented via help strings. To get more information about a DIPLOMAT subcommand or command, simply run it with the <code>-h</code> or <code>--help</code> flag.</p>
            <div class="commands">
                <pre># Help for all of DIPLOMAT (lists subcommands of DIPLOMAT):
diplomat --help 
# Help for the track subcommand:
diplomat track --help
# Help for the predictors subcommand space:
diplomat predictors --help</pre>
            </div>
        </section>

        <section>
            <h2>Documentation</h2>
            <p>DIPLOMAT has documentation on ReadTheDocs at <a href="https://diplomat.readthedocs.io/en/latest" target="_blank">https://diplomat.readthedocs.io/en/latest</a>.</p>
        </section>

        <section>
            <h2>Development</h2>
            <p>DIPLOMAT is written entirely in Python. To set up an environment for developing DIPLOMAT, you can simply pull down this repository and install its requirements using pip. For a further description of how to set up DIPLOMAT for development, see the <a href="https://diplomat.readthedocs.io/en/latest/advanced_usage.html#development-usage" target="_blank">Development Usage</a> section in the documentation.</p>
        </section>

        <section>
            <h2>Contributing</h2>
            <p>We welcome external contributions, although it is a good idea to contact the maintainers before embarking on any significant development work to make sure the proposed changes are a good fit.</p>
            <p>Contributors agree to license their code under the license in use by this project (see <code>LICENSE</code>).</p>
            <p>To contribute:</p>
            <ol>
                <li>Fork the repo</li>
                <li>Make changes on a branch</li>
                <li>Create a pull request</li>
            </ol>
        </section>

        <section class="author-contact">
            <h2>Authors</h2>
            <p>If you have any questions, feel free to reach out to Isaac Robinson, at <a href="mailto:isaac.k.robinson2000@gmail.com">isaac.k.robinson2000@gmail.com</a></p>
            <p>See <code>AUTHORS</code> for the full list of authors.</p>
        </section>
    </div>

    <footer>
        <p>&copy; 2024 DIPLOMAT Project</p>
        <p>See <code>LICENSE</code> for details.</p>
    </footer>
</body>
</html>
